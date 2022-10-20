mkdir %USERPROFILE%\1dir_manager 
copy %CD%\mapping.json %USERPROFILE%\dir_manager
%CD%\nssm-2.24\win64\nssm.exe install "DIR-Manager" "%CD%\python\Scripts\python.exe" "%CD%\dManager.py" "%USERPROFILE%"
%CD%\nssm-2.24\win64\nssm.exe  set "DIR-Manager" AppStdout "%USERPROFILE%\dir_manager\out_file.txt"
%CD%\nssm-2.24\win64\nssm.exe set "DIR-Manager" AppStderr "%USERPROFILE%\dir_manager\error_file.txt"