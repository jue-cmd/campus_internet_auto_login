import json
import copy

class Config:
	@staticmethod
	def boostrap(json_name="confs.json"):
		with open("config"+json_name) as f:
			confs = json.load(f)
			Config.config = confs
			return Config.config
	@staticmethod
	def get_config():
		if hasattr(Config, "config"):
			return Config.config
		else:
			return Config.boostrap()
	@staticmethod
	def copy_current_config():
		return copy.deepcopy(Config)