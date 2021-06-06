# Summary
This is meant as an environment for me to play with and benchmark different programming languages, 
as well as practice the use of some general tools. 

## Problem Definition
The environment shall provide a somewhat realistic problem to solve, as well as
 loadtests to benchmark and compare solutions. 

* There exists an SQL Database containing Company Information
* There exist two systems returning non-overlapping userdata via REST APIs
* Users have internal Identifiers as well as UUID that is unique accross systems
* Users in both systems have a relation to a Company UUID

A new system shall offer a REST API allowing to: 
* Access a User enriched with Company data by User UUID
* Acces a list of Users by Company UUID

# Why
I want an actual problem to solve, while trying out programming languages I find interesting. 

I also want to gain a deeper understanding of a solutions performance, 
not just in terms of writing, but also running the code. 
Thus a loadtest that can be run against solutions shall serve as a benchmarking tool. 

# Goals
* Setup two User API mocks - using [killgrave](https://github.com/friendsofgo/killgrave)
* Setup a Company Database - using sqlite
* Setup a benchmarking loadtest - using locust
* Write a baseline 'enterprise default' solution in Java
* Write a solution in Go
* Write a solution in Elixir
* Use this as a go-to sample problem to try out any interesting language 

# Non-Goals
* Get too deep into "framework" tools (API mocking, testing, ..)
