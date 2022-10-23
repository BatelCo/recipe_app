const recipeRender = function () {
	const renderPage = function (res) {
		renderComponent("#recipe-template", "#results", res.metaData)
	}

	const renderComponent = function (hbTemplate, elementToRender, metaData) {
		const source = $(hbTemplate).html()
		const template = Handlebars.compile(source)
		let newHTML = template({ recipeData: metaData })
		$(elementToRender).empty()
		$(elementToRender).append(newHTML)
	}

	return {
		renderPage,
		renderComponent,
	}
}