$(function($) {
    var app = {};

    var dummy_data = {
        'events': [
            {'id': Math.floor(Math.random() * 1000 % 1000), 'application': 'Gmail', 'description': 'Email to jony@apple.com',
             'start': new Date(2016, 1, 11, 9, 4, 20), 'end': new Date(2016, 1, 11, 9, 50, 55)},
            {'id': Math.floor(Math.random() * 1000 % 1000), 'application': 'Word', 'description': 'APPL_INC_MARKETING_V1',
             'start': new Date(2016, 1, 11, 10, 15, 20), 'end': new Date(2016, 1, 11, 11, 25, 55)},
            {'id': Math.floor(Math.random() * 1000 % 1000), 'application': 'Excel', 'description': 'CocaCola_Prospective_Partners',
             'start': new Date(2016, 1, 11, 13, 40, 43), 'end': new Date(2016, 1, 11, 15, 04, 01)},
        ],
        'projects': [
            {'client': 'Apple Inc.', 'project_name': 'Marketing Project'},
            {'client': 'Coca Cola Co.', 'project_name': 'Sales sourcing'},
        ]
    };

    var Event = Backbone.Model.extend({
        defaults: {
            id: 1,
            application: 'NA',
            name: 'No description available',
        }
    });

    var Events = Backbone.Collection.extend({
        model: Event,
    });

    var EventView = Backbone.View.extend({
        template: _.template(`<div id="<%= id %>" class="draggable-event label" draggable="true" ondragstart="app.drag(event)">
                             <%= application %>: <%= description %><br>
                             From: <%= start %> To: <%= end %> </div>`
        ),
        render: function() {
            this.$el.html(this.template(this.model.attributes));
            return this;
        },
    });

    var EventsView = Backbone.View.extend({
        el: $("div#calendar-container > .draggable-container"),

        initialize: function() {
            this.collection = new Events(dummy_data.events);
            this.render();
        },

        render: function() {
            _.each(this.collection.models, function(item) {
                this.renderEvent(item);
            }, this);
        },

        renderEvent: function(item) {
            var eventView = new EventView({
                model: item
            });
            this.$el.append(eventView.render().el);
        }
    });

    app.eventsView = new EventsView();

    app.allowDrop = function allowDrop(ev) {
        ev.preventDefault();
    }

    app.drag = function drag(ev) {
        ev.dataTransfer.setData("text", ev.target.id);
    }

    app.drop = function drop(ev) {
        ev.preventDefault();
        var data = ev.dataTransfer.getData("text");
        ev.target.appendChild(document.getElementById(data));
    }
    this.app = app;
});
