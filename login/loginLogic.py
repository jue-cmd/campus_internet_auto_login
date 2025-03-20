import internrtBase

def stat(imp: internrtBase.InterNetLogin) -> bool:
	return imp.check_internet_connection()

def login(imp: internrtBase.InterNetLogin, config: dict) -> bool | internrtBase.InterNetLogin:
	return imp.login(config['username'], config['password'])

def logout(imp: internrtBase.InterNetLogin, config: dict) -> bool | internrtBase.InterNetLogin:
	return imp.logout()