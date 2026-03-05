import {
  PropsWithChildren,
  createContext,
  useContext,
  useEffect,
  useState,
} from 'react'
import { apiFetch } from './api/client'

type User = {
  id: number
  username: string
  first_name: string
  last_name: string
  email: string
  role: string
} | null

type AuthContextValue = {
  user: User
  setUser(user: User): void
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined)

export function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<User>(null)

  useEffect(() => {
    apiFetch<User>('/auth/me/')
      .then((data) => setUser(data))
      .catch(() => setUser(null))
  }, [])

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) {
    throw new Error('useAuth must be used within AuthProvider')
  }
  return ctx
}

