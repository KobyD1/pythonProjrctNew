Feature: Calculator - Add

  Background:
    Given init calculator

#  @sanity
  Scenario: Adding action for positive numbers
    When set first number
    When set second number
    Then get the numbers summery results

    Scenario: Adding action for positive numbers
      When set first number
      When set third number
      Then get the numbers summery results
