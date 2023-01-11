# Discord Cache Exporter
A simple Python script that will export all of your Discord's cache directory into their original, readable filetypes

## Pip dependencies
- `filetype`

## How to use
1. Download the Python script
2. Install the required dependency by running `pip install filetype --user`
3. Run the script, `python ./discordCacheExport.py`
4. Wait until it's finished and look for the newly created directory called "exports"

Once finished, a summery should have been produced: 
```
...
Exporting complete!
490 files exported successfully
5 files failed to export
565 files detected in cache
Took 2459 milliseconds to complete

Exported files can be found in the exports/1673470087447 directory
```

Export folders are labeled with a "Milliseconds since Unix Epoch" timestamp of when you ran the script
