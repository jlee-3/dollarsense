export as namespace Ds

export interface Expense {
  id?: string
  description: string
  amount: number
  spotRate?: number
  currency: string
  category: string
  subCategory?: string
  createdAt?: Date
  updatedAt?: Date
}
