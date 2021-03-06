	<!-- Reservation modal -->
	<div class="modal fade" id="reservationModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	  <div class="modal-dialog">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
	        <h4 class="modal-title" id="myModalLabel">Uusi varaus</h4>
	      </div>
	      <div class="modal-body">
		  <h4>Alkamisajankohta: *</h4>
			<input type="text" class="glDateBox form-control" id="dateBox_modal" gldp-id="dateBox_modal"></input>
		    <div gldp-el="dateBox_modal" style="width:400px; height:300px; position:fixed; top:0px; left:0px;"></div>
	      <h4>Tarpeellisia lisätietoja: *</h4>
	      <textarea class="form-control" rows="4"></textarea>
	      </div>
	      <div class="modal-footer">
	      	<p class="pull-left">* = Pakollinen kenttä</p>
	        <button type="button" class="btn btn-default" data-dismiss="modal">Peruuta</button>
	        <button type="button" class="btn btn-primary" data-dismiss="modal">Tee varaus</button>
	      </div>
	    </div>
	  </div>
	</div>