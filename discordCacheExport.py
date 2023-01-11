import os
import time
import filetype

def main():
	dir = f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\discord\\Cache'
	print(f'Discovering files from Discord cache directory: {dir}')
	files = os.listdir(dir)
	print(f'Found {len(files)} files in cache directory')

	currentEpoch = round(time.time() * 1000)
	if not os.path.exists(f'exports/{currentEpoch}'):
		os.makedirs(f'exports/{currentEpoch}')

	completed = 0
	failed = 0
	beginTimestamp = currentEpoch

	for file in files:
		filePath = f'{dir}\\{file}'
		try:
			kind = filetype.guess(filePath)
			if kind is not None:
				print(f'Exporting {file}.{kind.extension}...')
				with open(f'exports/{currentEpoch}/{file}.{kind.extension}', 'wb') as f:
					f.write(open(filePath, 'rb').read())

				completed += 1
				f.close()
		except:
			failed += 1
			print(f'Failed to export {file}, probably not something that cannot be exported (E.g. data_XX or index files)')
			pass

	print('\nExporting complete!')
	print(f'{completed} files exported successfully')
	print(f'{failed} files failed to export')
	print(f'{len(files)} files detected in cache')
	print(f'Took {round(time.time() * 1000) - beginTimestamp} milliseconds to complete\n')
	print(f'Exported files can be found in the exports/{currentEpoch} directory')

if __name__ == '__main__':
	main()
