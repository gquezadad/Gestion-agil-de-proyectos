var RegionesYciudad = {

	"regiones": [{
			"NombreRegion": "Arica y Parinacota",
			"ciudad": ["Arica"]
	},
		{
			"NombreRegion": "Tarapacá",
			"ciudad": ["Iquique"]
	},
		{
			"NombreRegion": "Antofagasta",
			"ciudad": ["Antofagasta"]
	},
		{
			"NombreRegion": "Atacama",
			"ciudad": ["Copiapó"]
	},
		{
			"NombreRegion": "Coquimbo",
			"ciudad": ["La Serena"]
	},
		{
			"NombreRegion": "Valparaíso",
			"ciudad": ["Valparaíso"]
	},
		{
			"NombreRegion": "Región del Libertador Gral. Bernardo O’Higgins",
			"ciudad": ["Rancagua"]
	},
		{
			"NombreRegion": "Región del Maule",
			"ciudad": ["Talca"]
	},
		{
			"NombreRegion": "Región del Biobío",
			"ciudad": ["Concepción"]
	},
		{
			"NombreRegion": "Región de la Araucanía",
			"ciudad": ["Temuco"]
	},
		{
			"NombreRegion": "Región de Los Ríos",
			"ciudad": ["Valdivia"]
	},
		{
			"NombreRegion": "Región de Los Lagos",
			"ciudad": ["Puerto Montt"]
	},
		{
			"NombreRegion": "Región Aisén del Gral. Carlos Ibáñez del Campo",
			"ciudad": ["Coihaique"]
	},
		{
			"NombreRegion": "Región de Magallanes y de la AntárVca Chilena",
			"ciudad": ["Punta Arenas"]
	},
		{
			"NombreRegion": "Región Metropolitana de Santiago",
			"ciudad": ["Santiago"]
	},
	{
		"NombreRegion": "Online",
		"ciudad": ["Online"]
	}]
}


jQuery(document).ready(function () {

	var iRegion = 0;
	var htmlRegion = '<option value="Online">Seleccione región</option>';
	var htmlCiudad = '<option value="Online">Seleccione ciudad</option>';

	jQuery.each(RegionesYciudad.regiones, function () {
		htmlRegion = htmlRegion + '<option value="' + RegionesYciudad.regiones[iRegion].NombreRegion + '">' + RegionesYciudad.regiones[iRegion].NombreRegion + '</option>';
		iRegion++;
	});

	jQuery('#regiones').html(htmlRegion);
	jQuery('#ciudad').html(htmlCiudad);

	jQuery('#regiones').change(function () {
		var iRegiones = 0;
		var valorRegion = jQuery(this).val();
		var htmlCiudad = '<option value="Online">Seleccione ciudad</option>';
		jQuery.each(RegionesYciudad.regiones, function () {
			if (RegionesYciudad.regiones[iRegiones].NombreRegion == valorRegion) {
				var iCiudad = 0;
				jQuery.each(RegionesYciudad.regiones[iRegiones].ciudad, function () {
					htmlCiudad = htmlCiudad + '<option value="' + RegionesYciudad.regiones[iRegiones].ciudad[iCiudad] + '">' + RegionesYciudad.regiones[iRegiones].ciudad[iCiudad] + '</option>';
					iCiudad++;
				});
			}
			iRegiones++;
		});
		jQuery('#ciudad').html(htmlCiudad);
	});
	

});
// utilizado para rellenar los campos region y ciudad de acuerdo a la region seleccionada

