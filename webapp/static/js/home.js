hk = hk || {};

hk.ClientCollection = BB.Collection.extend({
    url: '/api/get_clients/'
});

hk.HomeView = BB.View.extend({
    el: '#home',
    template: _.template($('#home-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.model = new BB.Model({
            users: [
                {
                    first_name: 'Dan',
                    last_name: 'Borstelmann',
                    date_created: 'October 20 2016',
                    why: 'About to become homesless need help now, to become homesless need help now, to become homesless need help now',
                    date_of_birth: 'May 20 1972',
                    gender: 'Male',
                    veteran: 'No',
                    phone: '456-879-9760',
                    email: 'test@test.com',
                    family: 'Individual'
                },
                {
                    first_name: 'Dan',
                    last_name: 'Borstelmann',
                    date_created: 'October 20 2016',
                    why: 'About to become homesless need help now',
                    date_of_birth: 'May 20 1972',
                    gender: 'Male',
                    veteran: 'No',
                    phone: '456-879-9760',
                    email: 'test@test.com',
                    family: 'Family'
                },
            ],
            shelters: [
                {
                    name: 'Homeless Shelter',
                    address: '234 N 19th St.',
                    max_occupancy: '25',
                    occupancy: '20',
                    last_updated: '10 minutes ago'
                },
                {
                    name: 'Emergency Center',
                    address: '6794 Olive Ave.',
                    max_occupancy: '72',
                    occupancy: '37',
                    last_updated: '2 minutes ago'
                }
            ]
        });

        this.$el.empty().append(this.template(this.model.toJSON()));

        this.clientList = new hk.ClientCollection();
        this.clientSearchView = new hk.ClientSearchView({
            collection: this.clientList
        });

        this.profileView = new hk.ProfileView({
            model: this.model
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
        'keyup #client-search': 'searchStart'
    },

    openProfile: function (e) {
        this.clientSearchView.hide();
        this.profileView.show();

        setTimeout(function () {
            hk.materializeShit();
        }, 500);
    },

    markReviewed: function (e) {
        //Mark as reviewed
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

        if (e.which == 13 && !e.shiftKey) {
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
        this.render();
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
