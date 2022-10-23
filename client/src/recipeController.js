const model = RecipeModel()
const renderer = recipeRender()

const generateData = function (attempts = 0){
	model.getData().then((res) => {
			renderer.renderPage(res)
			return res
		})
		.catch((error) => {
			console.log(error)
			if (attempts++ < 3) {
				console.warn(`coudlnt load user.\n
                Attampts left: ${3 - attempts}\n
                trying again...`)
				generateData(attempts)
			} else {
				console.log(`attampet limit reached, please check whats wrong`)
			}
		})
}

const inputClear = function(){
	$("#ingredient").val("")
	$(':checkbox:checked').prop('checked',false);
}

$("#submit").on("click", function () {
	const ingredient = $("#ingredient").val()
	const glutenFree = $("#gluten-free").is(":checked")
	const dairyFree = $("#diary-free").is(":checked")
	if (ingredient != "") {
		model.initData(ingredient, glutenFree, dairyFree)
		generateData()
	} else console.warn("no input")
	inputClear()
})
