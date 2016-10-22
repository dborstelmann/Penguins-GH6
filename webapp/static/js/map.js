hk = hk || {};

hk.MapView = BB.View.extend({
    el: '#map',
    template: _.template($('#map-template').html()),

    initialize: function (options) {
    	this.render();
    },
    render: function(){
    	this.$el.empty().append(this.template());

     	 $.getJSON("/static/js/test_data.json", function (data) {

        // Correct UK to GB in data
        $.each(data, function () {
            if (this.code === 'UK') {
                this.code = 'GB';
            }
        });

        $('#container').highcharts('Map', {
            chart : {
                borderWidth: 1,
                map: 'custom/US'
            },

            title: {
                text: 'Ben Test Map'
            },

            subtitle: {
                text: 'GlobalHack VI'
            },

            legend: {
                enabled: false
            },

            mapNavigation: {
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'bottom'
                }
            },

            series: [{
                name: 'Countries',
                color: '#E0E0E0',
                enableMouseTracking: false
            }, {
                type: 'mapbubble',
                name: 'Population 2013',
                joinBy: ['iso-a2', 'code'],
                data: data,
                minSize: 4,
                maxSize: '12%',
                tooltip: {
                    pointFormat: '{point.code}: {point.z} thousands'
                }
            }]
        });

    });   
    }
});
