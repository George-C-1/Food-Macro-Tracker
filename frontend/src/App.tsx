import { useState } from 'react'
import AddMeal from './components/addMeal.tsx'

function App() {
  const [componentDisplay, setComponentDisplay] = useState<'addMeal' | 'createMeal' | 'createFood'>('addMeal');

  return (
    <>
      <h1>Welcome to the food nutrient tracker app</h1>
      <p>Track and analyze the nutritional content of your meals with ease!</p>
      <button onClick={() => setComponentDisplay('addMeal')}>Add Meal/ Snack</button>
      <button onClick={() => setComponentDisplay('createMeal')}>Create Meal</button>
      <button onClick={() => setComponentDisplay('createFood')}>Create food</button>
      <div>
        {/* Your app components will go here */}
        {componentDisplay === 'addMeal' && <AddMeal />} 
        {componentDisplay === 'createMeal' && <div>Create Meal Component Placeholder</div>}
        {componentDisplay === 'createFood' && <div>Create Food Component Placeholder</div>}
        
      </div>
    </>
  )
}

export default App
