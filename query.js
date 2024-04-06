function submitQuery() {
    var query = document.getElementById("queryInput").value;
    if (query.trim() !== "") {
        // Here you can perform actions with the submitted query,
        // like sending it to a server for processing or displaying it on the page.
        displayQueryResult(query);
        document.getElementById("queryInput").value = ""; // Clear the input field after submission
    }
}

function displayQueryResult(query) {
    var queryResultsDiv = document.querySelector(".query-results");
    var resultParagraph = document.createElement("p");
    resultParagraph.textContent = "Query: " + query;
    queryResultsDiv.appendChild(resultParagraph);
}
