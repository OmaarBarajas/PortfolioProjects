SELECT * FROM Corona..CovidDeaths
order by location, date

--SELECT location,date,total_cases, new_cases,total_deaths, population
--FROM Corona..CovidDeaths as CD
--order by location, date

-- Total cases vs Total Deaths (Case Fatality Rate) in Mexico
SELECT location,date,total_cases,total_deaths,(cast(total_deaths as int)/total_cases)*100 as CFR
FROM Corona..CovidDeaths
where location = 'Mexico'
order by location, date

--Total cases vs Population in Mexico
SELECT location,date,total_cases,Population,(total_cases/population)*100 as InfectionRate
FROM Corona..CovidDeaths
where location = 'Mexico'
order by location, date

--Percentage of Infection per country
SELECT location,Population,max(total_cases) as HighestInfection, Max((total_cases/population))*100 as PopulationInfected
FROM Corona..CovidDeaths
group by location, population
order by PopulationInfected desc

--Countries with highest death count 
SELECT location,max(total_deaths) as HighestDeaths
FROM Corona..CovidDeaths
where continent is not null
group by location
order by HighestDeaths desc

--Death count per Continent
SELECT continent,max(total_deaths) as Deathcount
FROM Corona..CovidDeaths
where continent is not null
group by continent
order by Deathcount desc

-- Actual Global Information
SELECT date,sum(new_cases)as TotalNewCases,sum(cast(new_deaths as int)) as TotalNewDeaths,(sum(cast(new_deaths as int))/sum(cast(new_cases as int)))*100 as CFRperDay
FROM Corona..CovidDeaths
where continent is not null
group by date
order by date

--Total population Vaccinated
Select CD.continent, CD.location,CD.date,CD.population,CT.new_vaccinations, SUM(CT.new_vaccinations) over (Partition by CD.location)
from Corona..CovidDeaths as CD
join Corona..CovidTests as CT
	On CD.location = CT.location
	and CD.date = CT.date
where CD.continent is not null
order by 2,3
