class MetaDataApi extends Api {
	constructor(ingridient = "cheese", diaryFree = false, glutenFree = false, apiInterface = new AjaxCall()) {
		let url = `http://localhost:8000/recipes?ingridient=${ingridient}&diaryFree=${diaryFree}&glutenFree=${glutenFree}`
		super(apiInterface, url)
	}

	async getData() {
		return await this.callApi()
	}
}