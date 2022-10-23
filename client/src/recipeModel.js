const RecipeModel = function () {
	let recipeMetaInstance
	let cacheData

	function getCache() {
		return cacheData
	}

	function initData(ingridient, diaryFree, glutenFree) {
		recipeMetaInstance = new MetaDataApi(ingridient, diaryFree, glutenFree)
	}

	async function getData() {
		let promise =  recipeMetaInstance.getData()
		return await Promise.all([promise]).then(function (results) {
			cacheData = results[0]
			return { metaData: results[0] }
		})
	}
	
	return {
		getCache,
		getData,
		initData,
	}
}