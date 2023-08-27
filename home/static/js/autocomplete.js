class AutocompleteHandler {
    start() {
        this.hideOriginalCountryInput()
        this.hideOriginalCountryInputupd()
        this.hideOriginalCountryInputProfile()
        this.onInitAutocomplete()
    }

    onInitAutocomplete() {
        new Autocomplete('#autocomplete', {
            search: (input) => {
                return this.onSearchCountry(input)
            }
        })
    }

    hideOriginalCountryInput() {
        const $originalCountryInput = document.querySelector('.post_form p:has(input[name=recipe_country])')
        if ($originalCountryInput){
            $originalCountryInput.remove()
        }
    }

    hideOriginalCountryInputupd() {
        const $originalCountryInputupd = document.querySelector('.update_form p:has(input[name=recipe_country])')
        if ($originalCountryInputupd){
            $originalCountryInputupd.remove()
        }
    }


    hideOriginalCountryInputProfile() {
        const $originalCountryInputProfile = document.querySelector('.updatepro_form .controls:has(input[name=country])')
        if ($originalCountryInputProfile){
            $originalCountryInputProfile.remove()
        }
    }

    onFilterCountriesResponse(data, input) {
        if (!data) {
            return []
        }
    
        return data
            .filter(({ name: { common } }) => {
                const regex = new RegExp(input, 'gi')
                return common.match(regex)
            })
            .map(({ name: { common } }) => common)
    }

    onSearchCountry(input) {
        if (!input) {
            return Promise.resolve([])
        }
    
        const url = `https://restcountries.com/v3.1/name/${input}?fields=name`
    
        return new Promise((resolve) => {
            fetch(url)
                .then(response => response.json())
                .then((data) => {
                    if (data.status === 404) {
                        return resolve([])
                    }
                    resolve(this.onFilterCountriesResponse(data, input))
                })
                .catch(() => {
                    resolve([])
                })
        })
    }
}

const autocompleteHandler = new AutocompleteHandler()
autocompleteHandler.start()
