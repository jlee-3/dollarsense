import { gql } from '@apollo/client/core'

export const expenseQueryGql = gql`
  query Expenses($input: ExpenseQueryInput!) {
    expenses(input: $input) {
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
        description
        currency
      }
    }
  }
`

export const editExpenseMutationGql = gql`
  mutation EditExpense($input: EditExpenseInput!) {
    editExpense(input: $input) {
      expense {
        id
        description
        currency
      }
    }
  }
`

export const deleteExpenseMutationGql = gql`
  mutation DeleteExpense($input: DeleteExpenseInput!) {
    deleteExpense(input: $input) {
      output {
        isSuccess
        affectedEntities
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
