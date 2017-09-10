var app1 = new Vue({
	el: '#app-1', delimiters: ['[[', ']]'],
	data: { message: 'Hello Vue.js!' }
});

var app2 = new Vue({
	el: '#app-2',
	data: { message: 'You loaded this page on ' + new Date() }
});

var app3 = new Vue({
	el: '#app-3',
	data: { seen: true }
});

var app4 = new Vue({
	el: '#app-4', delimiters: ['[[', ']]'],
	data: {
		todos: [
			{ text: 'Learn JavaScript' },
			{ text: 'Learn Vue' },
			{ text: 'Build something awesome' }
		]
}
});

var app6 = new Vue({
	el: '#app-6', delimiters: ['[[', ']]'],
	data: { message: 'Hello Vue.js!' }
});

var app5 = new Vue({
	el: '#app-5', delimiters: ['[[', ']]'],
	data: { message: app6.message },
	methods: {
		reverseMessage: function () {
			this.message = app6.message.split('').reverse().join('')
			app6.message = this.message
		}
	}
});

// Define a new component called todo-item
Vue.component('todo-item', {
	props: ['todo'], delimiters: ['[[', ']]'],
	template: '<li>[[ todo.text ]]</li>'
});

var app7 = new Vue({
	el: '#app-7',
	data: {
		groceryList: [
			{ id: 0, text: 'Vegetables' },
			{ id: 1, text: 'Cheese' },
			{ id: 2, text: 'Whatever else humans are supposed to eat' }
		]
	}
});

var app8 = new Vue({
	el: '#app-8', delimiters: ['[[', ']]'],
	data: { username: '' },
	methods: {
		onSubmit(event) {
			if (this.username && this.username !== '') {
					this.username = 'Submited'
			}
		}
	}
});
