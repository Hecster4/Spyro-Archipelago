import ctypes
from ctypes import wintypes

INVALID_HANDLE_VALUE = -1

class PROCESSENTRY32W(ctypes.Structure):
    _fields_ = [
        ("dwSize",              wintypes.DWORD),
        ("cntUsage",            wintypes.DWORD),
        ("th32ProcessID",       wintypes.DWORD),
        ("th32DefaultHeapID",   ctypes.POINTER(wintypes.ULONG)),
        ("th32ModuleID",        wintypes.DWORD),
        ("cntThreads",          wintypes.DWORD),
        ("th32ParentProcessID", wintypes.DWORD),
        ("pcPriClassBase",      wintypes.LONG),
        ("dwFlags",             wintypes.DWORD),
        ("szExeFile",           ctypes.c_wchar * 260)
        ]

class MODULEENTRY32W(ctypes.Structure):
    _fields_ = [
        ("dwSize",        wintypes.DWORD),
        ("th32ModuleID",  wintypes.DWORD),
        ("th32ProcessID", wintypes.DWORD),
        ("GlblcntUsage",  wintypes.DWORD),
        ("ProccntUsage",  wintypes.DWORD),
        ("modBaseAddr",   ctypes.POINTER(wintypes.BYTE)), 
        ("modBaseSize",   wintypes.DWORD),
        ("hModule",       wintypes.HMODULE),
        ("szModule",      ctypes.c_wchar * 256),        
        ("szExePath",     ctypes.c_wchar * 260)
        ]
    
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

kernel32.CreateToolhelp32Snapshot.argtypes = [wintypes.DWORD, wintypes.DWORD]
kernel32.CreateToolhelp32Snapshot.restype = wintypes.HANDLE

kernel32.Process32FirstW.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
kernel32.Process32FirstW.restype = wintypes.BOOL

kernel32.Process32NextW.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
kernel32.Process32NextW.restype = wintypes.BOOL

kernel32.OpenFileMappingW.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR]
kernel32.OpenFileMappingW.restype = wintypes.HANDLE

kernel32.MapViewOfFile.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, ctypes.c_size_t]
kernel32.MapViewOfFile.restype = wintypes.LPVOID

kernel32.GetCurrentProcess.argtypes = []
kernel32.GetCurrentProcess.restype = wintypes.HANDLE

kernel32.Module32FirstW.argtypes = [wintypes.HANDLE, ctypes.POINTER(MODULEENTRY32W)]
kernel32.Module32FirstW.restype = wintypes.BOOL

kernel32.Module32NextW.argtypes = [wintypes.HANDLE, ctypes.POINTER(MODULEENTRY32W)]
kernel32.Module32NextW.restype = wintypes.BOOL

kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
kernel32.OpenProcess.restype = wintypes.HANDLE

kernel32.ReadProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPVOID, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
kernel32.ReadProcessMemory.restype = wintypes.BOOL

kernel32.WriteProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPVOID, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
kernel32.WriteProcessMemory.restype = wintypes.BOOL

kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
kernel32.CloseHandle.restype = wintypes.BOOL


def CreateToolhelp32Snapshot(dwFlags, th32ProcessID):
    hSnapshot = wintypes.HANDLE(kernel32.CreateToolhelp32Snapshot(dwFlags, th32ProcessID))
    if hSnapshot == INVALID_HANDLE_VALUE:
        raise ctypes.WinError(ctypes.get_last_error())
    return hSnapshot

def Process32FirstW(hSnapshot, lppe):
    if not kernel32.Process32FirstW(hSnapshot, lppe):
        raise ctypes.WinError(ctypes.get_last_error())

def Process32NextW(hSnapshot, lppe):
    if not kernel32.Process32NextW(hSnapshot, lppe):
        raise ctypes.WinError(ctypes.get_last_error())
    
def OpenFileMappingW(dwDesiredAccess, bInheritHandle, lpName):
    hMapping = wintypes.HANDLE(kernel32.OpenFileMappingW(dwDesiredAccess, bInheritHandle, lpName))
    if hMapping == None:
        raise ctypes.WinError(ctypes.get_last_error())
    return hMapping

def MapViewOfFile(hFileMappingObject, dwDesiredAccess, dwFileOffsetHigh, dwFileOffsetLow, dwNumberOfBytesToMap):
    mapViewBaseAddress = wintypes.LPVOID(kernel32.MapViewOfFile(hFileMappingObject, dwDesiredAccess, dwFileOffsetHigh, dwFileOffsetLow, dwNumberOfBytesToMap))
    if mapViewBaseAddress == None:
        raise ctypes.WinError(ctypes.get_last_error())
    return mapViewBaseAddress

def GetCurrentProcess():
    pHandle = wintypes.HANDLE(kernel32.GetCurrentProcess())
    if pHandle == None:
        raise ctypes.WinError(ctypes.get_last_error())
    return pHandle
    
def Module32FirstW(hSnapshot, lppe):
    if not kernel32.Module32FirstW(hSnapshot, lppe):
        raise ctypes.WinError(ctypes.get_last_error())
    
def Module32NextW(hSnapshot, lppe):
    if not kernel32.Module32NextW(hSnapshot, lppe):
        raise ctypes.WinError(ctypes.get_last_error())
    
def OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId):
    pHandle = wintypes.HANDLE(kernel32.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId))
    if pHandle == None:
        raise ctypes.WinError(ctypes.get_last_error())
    return pHandle
    
def ReadProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize, lpNumberOfBytesRead):
    if not kernel32.ReadProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize, lpNumberOfBytesRead):
        raise ctypes.WinError(ctypes.get_last_error())
    
def WriteProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize, lpNumberOfBytesRead):
    if not kernel32.WriteProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize, lpNumberOfBytesRead):
        raise ctypes.WinError(ctypes.get_last_error())
    
def CloseHandle(hObject):
    if not kernel32.CloseHandle(hObject):
        raise ctypes.WinError(ctypes.get_last_error())
