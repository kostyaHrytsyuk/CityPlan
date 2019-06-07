<h1 align="center">Google Hash Code 2018 Final Round</h1>
<p align="center">
  <img src="event_google-hash-code_491696.jpg">
</p>

<h3 align="center">Description of the algorithms that were used</h3>
<hr>

To solve this problem, we used a combination of different paradigms in the development of algorithms, namely: Divide and conquere and Greedy algorithms.

We have used the "Divide and conquere" approach to break up one big task into much smaller similar subtasks. Instead of developing an algorithm that would fill the whole city with different buildings, we have developed algorithms for building an optimal block according to the task conditions. In order to achieve the greatest result, we need the maximum number of dwellings to be at a distance less than - equal to the Manhattan distance. Therefore, we decided that it would be advisable to build a quarter, which is perimeter filled with dwelling houses, and in the middle of communal.

It is when the yard is filled with communal houses we are using a greedy algorithm.

Passing through each point our algorithm looks around at Manhattan's distance in search of a residential building. When he finds the first neighbor, he begins to analyze the existing communes in this neighbor. When he finds a type which is not yet in the collection of communal buildings of a neighbor, he builds a communal building of this type if there is enough space for it.

The greed of this algorithm is as follows:
* The algorithm chooses a communal building relative to the first neighbor that he has found.
* The algorithm chooses a communal building of the first found of this type, which is not yet in the neighboring residential building.

<hr>

The basic algorithm that we implemented for solving the problem is the following steps:
1. At the first stage, we find the most up-to-date house of the type Residential. To do this we have introduced a special indicator, which is determined by the ratio of the capacity of the building to its size. We calculate the size of the city by calculating the Manhattan distance, that is, the distance from the right upper to the lower left corner.
2. In the second step, we form our neighborhood, from the houses that represent the most optimal residential building that we found in the previous step.
That is, our neighborhood can be described in words as 3 buildings horizontally 3 vertically but with a carved central building, in the place of which will be located communal facilities.
3. In the third step using the greedy algorithm, we fill the free space with the houses of the type Communal.
When a house like a communal building is being built, it looks around or around the house near which we want to build our communal house at a distance from the Manhattan distance are residential houses around which there are no communal facilities of this type yet, and if the situation looks like that, around that house we do not want to build. then he builds otherwise no.
4. In the fourth step, we fill our city with a quarter. That is, blocks, but each quarter represents the structure of the quarter that we created in the previous stage.

<h3 align="center">A table with the results of algorithms on different inputs</h3>
<hr>

| Data Set                |Score     |
|-------------------------|----------|
|a_example.in             |75        |
|b_short_walk.in          |536761    |
|c_going_green.in         |7222644   |
|d_wide_selection.in      |777888    |
|e_precise_fit.in         |2181080   |
|f_different_footprints.in|1566720   |
