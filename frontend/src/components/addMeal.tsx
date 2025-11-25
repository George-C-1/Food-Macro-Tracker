export function AddMeal(){
    // Function to handle adding a new ingredient
    return(
        <>
        <div>
            <h2>Add Meal</h2>
        </div>
        <form >
            <label htmlFor="mealName">Meal name</label>
            <input
            id="mealName"
            type="text"
            placeholder="Bolognese"
            required
            aria-label="Meal name"
            />

            {/* <button onClick={newIngredient}>New Ingredient</button> */}
            <button type="submit">Add</button>
        </form>
        </>
    )
}

export default AddMeal