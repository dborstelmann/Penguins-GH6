hk = hk || {};

hk.ClientCollection = BB.Collection.extend({
    url: '/api/get_clients/',
    modelId: function(attrs) {
        return attrs.id;
    }
});

hk.ProfileModel = BB.Model.extend({
    url: '/api/get_user/'
});

hk.ApplicationsCollection = BB.Collection.extend({
    url: '/api/get_applicants/',
    modelId: function(attrs) {
        return attrs.id;
    }
});

hk.SheltersCollection = BB.Collection.extend({
    url: '/api/get_shelters/',
    modelId: function(attrs) {
        return attrs.id;
    }
});

hk.HomeView = BB.View.extend({
    el: '#home',
    template: _.template($('#home-template').html()),

    initialize: function (options) {
        this.applicationsCollection = new hk.ApplicationsCollection();
        this.applicationsCollection.fetch();

        this.sheltersCollection = new hk.SheltersCollection();
        this.sheltersCollection.fetch();

        this.listenTo(this.applicationsCollection, 'sync', this.render);
        this.listenTo(this.sheltersCollection, 'sync', this.render);
    },

    render: function () {

        this.$el.empty().append(this.template({
            applicants: this.applicationsCollection.toJSON(),
            shelters: this.sheltersCollection.toJSON()
        }));
        hk.materializeShit();

        this.clientList = new hk.ClientCollection();
        this.clientSearchView = new hk.ClientSearchView({
            collection: this.clientList
        });

        this.profileModel = new hk.ProfileModel();
        this.profileView = new hk.ProfileView({
            model: this.profileModel
        });
    },

    searchClients: function (searchString) {
        this.clientList.fetch({
            type: 'POST',
            data: {
                query: searchString
            }
        });
    },

    events: {
        'click .logout': 'goHome',
        'click .profile-link': 'openProfile',
        'click .mark-reviewed': 'markReviewed',
        'keyup #available': 'updateOccupancy',
        'keyup #client-search': 'searchStart'
    },

    openProfile: function (e) {
        this.clientSearchView.hide();
        var $id = $(e.target).attr('data-id');

        this.profileModel.fetch({
            type: 'POST',
            data: {
                id: $id
            }
        });
    },

    updateOccupancy: function (e) {
        var $id = $(e.target).attr('data-id'),
            $val = $(e.target).val();

        if ($val === '') {
            return;
        }

        if (e.which == 13) {
            $(e.target).blur();

            $.ajax({
                url: '/api/update_shelter/',
                type: 'POST',
                data: {
                    id: $id,
                    occupancy: $val
                },
                success: function () {
                    Materialize.toast('Occupancy updated.', 2000);
                }
            });
        }
    },

    markReviewed: function (e) {
        var _this = this,
            $id = $(e.target).attr('data-id');

        $.ajax({
            url: '/api/mark_reviewed/',
            type: 'POST',
            data: {
                id: $id
            },
            success: function () {
                _this.applicationsCollection.fetch();
            }
        });
    },

    goHome: function () {
        $.ajax({
            url: '/auth/logout/',
            type: 'POST',
            success: function () {
                window.location.href = '/';
            }
        });
    },

    searchStart: function (e) {
        var $val = $(e.target).val();

        if ($val === '') {
            return;
        }

        if (e.which == 13) {
            e.preventDefault();
            $(e.target).blur();
            this.searchClients($val);
        }
    }
});

hk.ClientSearchView = BB.View.extend({
    el: '.search-modal-holder',
    template: _.template($('#search-template').html()),

    initialize: function (options) {
        this.listenTo(this.collection, 'sync', this.render);
    },

    render: function () {
        this.$el.empty().append(this.template({users: this.collection.toJSON()}));
        hk.materializeShit();
        this.show();
    },

    show: function () {
        this.$('.search-modal').openModal();
    },

    hide: function () {
        this.$('.search-modal').closeModal();
    },

    events: {
        'click .close-search': 'closeSearch'
    },

    closeSearch: function () {
        this.hide();
    },
});

hk.ProfileView = BB.View.extend({
    el: '.profile-modal-holder',
    template: _.template($('#profile-template').html()),

    initialize: function (options) {
        this.listenTo(this.model, 'sync', this.render);
    },

    render: function () {
        this.$el.empty().append(this.template(this.model.toJSON()));

        this.$('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 100 // Creates a dropdown of 15 years to control year
        });

        hk.materializeShit();
    },

    show: function () {
        this.$('.profile-modal').openModal();
    },

    hide: function () {
        this.$('.profile-modal').closeModal();
    },

    events: {
        'click .close-profile': 'closeProfile'
    },

    closeProfile: function () {
        this.hide();
    },
});
