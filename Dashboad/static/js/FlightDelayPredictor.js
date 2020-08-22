


d3.json("/get_origin_states", function(originStates) {
    d3Select = d3.select("#origin_states");

    d3Select.on("change", onChangeOrgStatesEventHandler);

    // Append select options to the select object for each filter data field unique value
    originStates.forEach((valueArray) => {
        if(valueArray !== null){
            d3Select.append("option").attr("value", valueArray[0]).text(valueArray[0]);
        }
    });

});

function clearSelectOptions(selectId){

    var select = document.getElementById(selectId);

    if (select !== null){

        for (i = select.length - 1; i >= 0; i--) {
            select.remove(i);
        }
    }
 }

function onChangeOrgStatesEventHandler(){

    originStateCode = d3.event.target.value;

    d3.json("/get_origin_state_airports?origin_state_code=" + originStateCode, (originStateAirports) => {
        
        selectId = "origin_state_airports"

        clearSelectOptions(selectId)

        d3Select = d3.select("#origin_state_airports")
 
        if (originStateAirports !== null){
            // Append select options to the select object for each filter data field unique value
            originStateAirports.forEach((valueArray) => {d3Select.append("option").attr("value", valueArray[1]).text(valueArray[0])});
        }
    
    });
}
