hk = hk || {};

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

        this.clientSearchView = new hk.ClientSearchView({
            model: this.model
        });

        this.profileView = new hk.ProfileView({
            model: this.model
        });
    },

    searchClients: function () {
        this.clientSearchView.show();
    },

    events: {
        'click .logout': 'goHome',
        'click .profile-link': 'openProfile',
        'keyup #client-search': 'searchStart'
    },

    openProfile: function () {
        this.clientSearchView.hide();
        this.profileView.show();
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
        if (e.which == 13 && !e.shiftKey) {
            e.preventDefault();
            $(e.target).blur();
            this.searchClients();
        }
    }
});

hk.ClientSearchView = BB.View.extend({
    el: '.search-modal-holder',
    template: _.template($('#search-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template(this.model.toJSON()));

        hk.materializeShit();
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
