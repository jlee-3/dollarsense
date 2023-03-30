import { gql } from '@apollo/client/core'

export const expenseQueryGql = gql`
  query AllExpenses {
    allExpenses {
      title
      amount
      currency
      category
      createdAt
      updatedAt
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
