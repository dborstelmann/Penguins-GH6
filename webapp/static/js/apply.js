hk = hk || {};

hk.ApplyView = BB.View.extend({
    el: '#apply',
    template: _.template($('#apply-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());

        this.$('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 100 // Creates a dropdown of 15 years to control year
        });
        hk.materializeShit();
    },

    events: {
        'click .home-link': 'goHome'
    },

    goHome: function () {
        window.location.href = '/';
    }
});
