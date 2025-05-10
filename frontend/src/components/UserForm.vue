<template>
  <div>
    <h2>User Info Form</h2>
    <form @submit.prevent="submitForm">
      <input v-model="name" placeholder="Name" required />
      <input v-model="family" placeholder="Family" required />
      <input v-model="age" type="number" placeholder="Age" required />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      name: '',
      family: '',
      age: ''
    }
  },
  methods: {
    async submitForm() {
      await axios.post('http://localhost:5000/api/user', {
        name: this.name,
        family: this.family,
        age: this.age
      });
      alert('User info submitted!');
      this.name = '';
      this.family = '';
      this.age = '';
    }
  }
}
</script>
