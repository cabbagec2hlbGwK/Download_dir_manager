@not done
# Download_dir_manager
Manage all of the files inside the download or any other location by relocating them based on tags or extension.
## Instalation
- Run CMD as Administrator and launch the "run.cmd" file.
- After that change the "target_dir" key in the  %USERPROFILE%\dir_manager\mapping.json to approprate location as this app will monitor that location 
## Usage
- File-tag mapping 
- all the mappings are saved at %USERPROFILE%\dir_manager\mapping.json
  - *Example*
    - "tmp":"C:/user/xyz/test/tempFiles" ("TAG":"PATH-WHERE-TO_MOVE") This will move any files with "tmp" in the file name.
    
