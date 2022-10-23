const RecipeModel = function () {
	let recipeMetaInstance
	let cacheData

	function getCache() {
		return cacheData
	}

	function initData(ingridient = "cheese", diaryFree = false, glutenFree = false) {
		recipeMetaInstance = new MetaDataApi(ingridient, diaryFree, glutenFree)
	}

	async function getData() {
		let promise =  recipeMetaInstance.getData()
		return await Promise.all([promise]).then(function (results) {
			cacheData = results[0]
			console.log("recipemodel")
			console.log(cacheData)
			return { metaData: results[0] }
		})
	}
	
	return {
		getCache,
		getData,
		initData,
	}
}