import BlockLayer, sys, config, MemoryInterface

MemoryInterface.Initialize_My_FileSystem()
interface = BlockLayer.BlockLayer()


class Operations():
	def __init__(self):
		self.map = []

	#WRITES STRING1
	def write(self, string):
		data_array = []
		# verify that string is of type string
		for i in range(0, len(string), config.BLOCK_SIZE):
			# divide up the string into chunks of length BLOCK_SIZE
			data_array.append(string[i : i + config.BLOCK_SIZE])
		self.__write_to_filesystem(data_array)


	#READS THE STRING
	def read(self):
		data = []
		for i in range(len(self.map)):
			# index through block numbers in map to get data blocks
			data.append(interface.BLOCK_NUMBER_TO_DATA_BLOCK(self.map[i]))
		print( "".join(data))
		return "".join(data)

	#WRITE TO FILESYSTEM
	def __write_to_filesystem(self, data_array):
		for i in range(len(data_array)):
			valid_block_number = interface.get_valid_data_block()
			interface.update_data_block(valid_block_number, data_array[i])
			self.map.append(valid_block_number)

	#STATUS FUNCTION TO CHECK THE STATUS OF THE DATA BLOCKS IN THE MEMORY
	def status(self):
		print(MemoryInterface.status())

	# WRITE TO OFFSET (refer to assignment doc)
	def write_to_offset(self,offset,string):
		index_to_write = offset / config.BLOCK_SIZE
		offerset_to_write = offset % config.BLOCK_SIZE
		length_to_write = len(string)
		while length_to_write > 0:
			if index_to_write >= len(self.map) :
					self.map.append(interface.get_valid_data_block())
			block_data = []
			block_data = interface.BLOCK_NUMBER_TO_DATA_BLOCK(self.map[index_to_write])
			string_to_write = list(block_data)
			if offerset_to_write != 0 :
				for index in range(config.BLOCK_SIZE - offerset_to_write):
					string_to_write[offerset_to_write + index] = string[len(string) - length_to_write]
					length_to_write = length_to_write - 1
				interface.update_data_block(self.map[index_to_write], "".join(string_to_write))	
			else :
				byte_to_write = min(length_to_write, 4)
				for index in range(byte_to_write):
					string_to_write[index] = string[len(string) - length_to_write]
					length_to_write = length_to_write - 1
				interface.update_data_block(self.map[index_to_write], "".join(string_to_write))
			offerset_to_write = 0
			index_to_write += 1
			
if __name__ == "__main__":
	if len(sys.argv) < 3: 
		print("Usage: python HW1.py <string1> <string2>")
		exit(0)
	test = Operations()
	test.write(sys.argv[1])
	test.read()
	test.status()
	test.write_to_offset(int(sys.argv[3]),sys.argv[2])
	test.read()
	# last call 
	test.status()
	

