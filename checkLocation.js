function checkLocation() {
    //let location = [form1.city.value, form1.state.value];
    var city, state, southDakota, northDakota, littleRock, oklahomaCity;
    city = document.form1.city.value;
    state = document.form1.state.value;
    
    southDakota = "South Dakota";
    northDakota = "North Dakota";
    littleRock = "Little Rock";
    oklahomaCity = "Oklahoma City";

    let tornadicCities = ["Huntsville", "Jackson", "Birmingham", "Tuscaloosa", 
        littleRock, "Tulsa", oklahomaCity, "okc", "Atlanta", "Wichita", "Nashville"];

    let tornadicState = ["Alabama", "Tennessee", "Oklahoma", "Arkansas", "Louisiana", "Texas", 
        "Missouri", "Kansas", "Georgia", southDakota, "Iowa", 
        "Minnesota", "Wisconsin", "Illinois", "Indiana", "Missouri", "Mississippi",
        "Arkansas", northDakota, "Montana", "Ohio", "Colorado", "Wyoming", "Nebraska"]; 

    for(var i = 0; i <= tornadicCities.length; i++)
    {
        if(tornadicCities.includes(city))
        {
            document.form1.likelihood.value = "Location likely to experience severe tornadoes";
        }
        else 
        {
            document.form1.likelihood.value = "Tornadoes less common but not impossible";
        }
    }

    for(var j = 0; j <= tornadicState.length; j++)
    {
        if(tornadicState.includes(state))
        {
            document.form1.likelihood.value = "Location likely to experience severe tornadoes";
        }
        else 
        {
            document.form1.likelihood.value = "Tornadoes less common but not impossible";
        }
    }
}