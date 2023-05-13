# copytool
copytool copies files hell-bent for leather

TeraCopy needs 4 minutes, copytool 6 seconds
![](https://github.com/hansalemaos/copytool/blob/main/fastcopyscreenshot.png?raw=true)

## CLI

      Example: copytool --src "C:\ProgramData\anaconda3\envs" --dst "e:\envbackup" --use_tqdm 1 --copy_date 1 --copy_permission 0 --overwrite 1
      --src                     str         (source folder)
      --dst                     str         (destination folder)
      --log                     str  ""     (csv log)
      --copy_date               int  0      (copy date stats)
      --copy_permission         int  0      (copy permissions)
      --use_tqdm                int  1      (show progress bar)
      --overwrite               int  1      (overwrite existing files in dst)


## Python

```python
from copytool import get_all_files_on_hdd_and_copy
get_all_files_on_hdd_and_copy(
    src = r"C:\path",
    dst = r"e:\dest",
    log = "c:\\copylog.csv",
    copy_date= 1,
    copy_permission= 0,
    use_tqdm = 1,
    overwrite = 1,
)     
```
