# MayaMoveKeyframes
a script to find the start time of a skeleton animation and move them to time 0

## How to Use
#### Single Convert
First, select your skeleton root, then run the python script
When running the script, change the `batchConvert()` at line 50 to `singleConvert()`

#### Batch Convert
In the script, the path is set from the project root directory.<br>
All the fbx files waiting for converting is in `rootDirectory/assets/inputs`<br>
The converted fbx will be written to `rootDirectory/assets/outputs` with the same name<br>

After the files are in the folder, can just run the script!
