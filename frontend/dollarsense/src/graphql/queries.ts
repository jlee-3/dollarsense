import { gql } from '@apollo/client/core'

export const expenseQueryGql = gql`
  query AllExpenses {
    allExpenses {
      id
      description
      amount
      spotRate
      currency
      category
      subCategory
      createdAt
      updatedAt
    }
  }
`

export const addExpenseMutationGql = gql`
  mutation AddExpense($input: AddExpenseInput!) {
    addExpense(input: $input) {
      expense {
        id
        title
        currency
      }
    }
  }
`

export const exampleQueryGql = gql`
  query Example($id: String!) {
    example(id: $id) {
      id
      type
      content
    }
  }
`
export const exampleMutationGql = gql`
  mutation ExampleMutation($input: ExampleInput!) {
    exampleMutation(input: $input) {
      field1
      field2
    }
  }
`
