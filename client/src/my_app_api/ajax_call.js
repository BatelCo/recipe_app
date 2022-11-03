class AjaxCall {
	async getApi(url, method = "GET", payload = "", resourcses = "") {
		let ajaxData = {
			url: url + resourcses,
			data: payload,
			success: (result) => result,
			error: (result) => "error",
			type: method,
		}
		return await $.ajax(ajaxData)
	}
}