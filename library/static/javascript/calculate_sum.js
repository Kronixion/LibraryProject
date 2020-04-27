var field_with_value = document.getElementsByName("price_item");
var sum = parseInt(0);

for(var x=0; x < field_with_value.length; x++)   // comparison should be "<" not "<="
{
    var removedText = parseInt(field_with_value[x].innerText.replace(/\D+/g, ''));
    sum = sum + removedText;
}

console.log(sum);

document.getElementById("total_price_sum_js").innerText = "$" + sum;
