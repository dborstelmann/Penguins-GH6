hk = hk || {};

hk.SheltersCollection = BB.Collection.extend({
    url: '/api/get_shelters/',
    modelId: function(attrs) {
        return attrs.id;
    }
});

hk.BedsView = BB.View.extend({
    el: '#beds',
    template: _.template($('#beds-template').html()),

    initialize: function (options) {
        this.sheltersCollection = new hk.SheltersCollection();
        this.sheltersCollection.fetch();

        this.listenTo(this.sheltersCollection, 'sync', this.render);
    },

    render: function () {
        this.$el.empty().append(this.template({shelters: this.sheltersCollection.toJSON()}));
    },
});
