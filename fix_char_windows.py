import os

root_dir = '.'

double_byte = ['é', 'ö', 'Á', 'à', 'ü', 'ç', 'ã', 'ô', 'Ü', 'ō', 'ñ', 'ý', 'á', 'ĕ', 'Ç', 'è', 'É', 'â', 'ú', 'ó', 'í', 'ê', 'ï', 'Ö', 'ä', 'À', 'ž', 'û']
single_byte = ['é', 'ö', 'Á', 'à', 'ü', 'ç', 'ã', 'ô', 'Ü', 'ō', 'ñ', 'ý', 'á', 'ĕ', 'Ç', 'è', 'É', 'â', 'ú', 'ó', 'í', 'ê', 'ï', 'Ö', 'ä', 'À', 'ž', 'û']

for file in os.listdir(root_dir):
	if file.endswith(".m3u8"):
		with open(file) as main:
			if not os.path.exists('cleaned'):
				os.makedirs('cleaned')
			write_file = os.path.join(root_dir, "cleaned", file)
			with open(write_file, 'w') as new_main:
				input_data = main.read()
				for i in range(0, len(double_byte)):
					input_data = input_data.replace(double_byte[i], single_byte[i])
				new_main.write(input_data)