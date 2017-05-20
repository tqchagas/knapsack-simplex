$('#resolver').click(function() {
	var form = $('#form_itens').serialize();
	$.ajax({
		url: '/knapsack/',
		type: 'POST',
		data: form,
		success: function(data) {
			alert('Status: ' + data.status + '\n' + 'Resposta: ' + data.resposta);
		},
		error: function (jqXHR, exception) {
			alert(jqXHR.responseJSON.erro);
		}
	});
});