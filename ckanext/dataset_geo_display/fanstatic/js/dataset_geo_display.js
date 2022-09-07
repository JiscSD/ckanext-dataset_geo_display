// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

ckan.module('map_module_display', function ($) {
  return {
    initialize: function () {
      var data = this.options.geojson;
      var map = L.map('map');
      L.tileLayer(
          'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: 'Data © <a href="http://osm.org/copyright">OpenStreetMap</a>',
          maxZoom: 18
      }).addTo(map);

      var result = L.geoJSON(data).addTo(map);

      map.fitBounds(result.getBounds());

      setInterval(() => {
          map.invalidateSize();
      }, 500);

    }
  };
});

