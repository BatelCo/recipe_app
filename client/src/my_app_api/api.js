class Api {
	url = ""
	method = ""
	proccesedData
	callerInteface

	constructor(callerInteface, url, method = "GET") {
		this.callerInteface = callerInteface
		this.url = url
		this.method = method
	}

	async callApi(attempts = 0) {
		return await this.callerInteface.getApi(this.url, this.method, this.data).catch((error) => {
			this.errorHandeler(this.callApi, attempts)
		})
	}

	errorHandeler(method, attempts) {
		if (attempts++ < 3) {
			console.warn(`error in : ${this.constructor.name} \n
                        Attampts left: ${3 - attempts}\n
                        trying again...`)
			return method(attempts)
		} else {
			console.log(`attampet limit reached, please check whats wrong`)
		}
	}

	processData(rawData) {
		this.proccesedData = rawData
		return this
	}
}