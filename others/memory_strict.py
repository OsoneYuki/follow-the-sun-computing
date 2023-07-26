import subprocess

def limit_memory_usage(max_memory_mb):
    job = subprocess.Popen(['cmd', '/c', 'start', '/B', 'python', 'fibonacci.py'],
                           creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NEW_PROCESS_GROUP)
    
    job_handle = job._handle
    
    # メモリ制限を設定する（メモリのサイズはバイト単位で指定）
    job_info = subprocess.STARTUPINFO()
    job_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    job_info.dwFlags |= subprocess.STARTF_USESTDHANDLES
    job_info.hStdInput = subprocess.PIPE
    job_info.hStdOutput = subprocess.PIPE
    job_info.hStdError = subprocess.PIPE

    extended_info = subprocess.STARTUPINFO()
    extended_info.lpAttributeList = job_info

    job_handle.SetInformationJobObject(subprocess.JobObjectExtendedLimitInformation, extended_info)

    # メモリ制限を設定
    memory_limit = int(max_memory_mb) * 1024 * 1024  # バイトに変換
    job_handle.SetExtendedLimitInformation({
        'BasicLimitInformation': {
            'LimitFlags': 0x200,
            'PeakProcessMemoryUsed': memory_limit,
            'MinimumWorkingSetSize': memory_limit,
            'MaximumWorkingSetSize': memory_limit
        }
    })

if __name__ == "__main__":
    max_memory_mb = 1024  # メモリ制限を1GBに設定
    limit_memory_usage(max_memory_mb)
