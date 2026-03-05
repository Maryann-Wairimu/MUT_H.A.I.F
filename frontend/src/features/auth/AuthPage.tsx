import { FormEvent, useState } from 'react'
import { apiFetch } from '../../api/client'
import { useAuth } from '../../authContext'

type LoginResponse = {
  id: number
  username: string
  first_name: string
  last_name: string
  email: string
  role: string
}

export function AuthPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const { setUser } = useAuth()

  async function handleSubmit(event: FormEvent) {
    event.preventDefault()
    setError(null)
    setLoading(true)
    try {
      const user = await apiFetch<LoginResponse>('/auth/login/', {
        method: 'POST',
        body: JSON.stringify({ username, password }),
      })
      setUser(user)
    } catch (err) {
      setError((err as Error).message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-md rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-sm shadow-slate-950/40">
      <h1 className="text-lg font-semibold text-slate-50">Sign in</h1>
      <p className="mt-1 text-xs text-slate-300">
        Use your university account to access hostel allocation and finance
        services.
      </p>
      <form onSubmit={handleSubmit} className="mt-4 space-y-3">
        <div>
          <label className="block text-xs font-medium text-slate-200">
            Username
          </label>
          <input
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-900 px-2 py-1.5 text-xs text-slate-50 outline-none ring-0 focus:border-emerald-500"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-200">
            Password
          </label>
          <input
            type="password"
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-900 px-2 py-1.5 text-xs text-slate-50 outline-none ring-0 focus:border-emerald-500"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        {error && (
          <p className="text-xs text-red-400" role="alert">
            {error}
          </p>
        )}
        <button
          type="submit"
          disabled={loading}
          className="mt-2 inline-flex w-full items-center justify-center rounded-md bg-emerald-500 px-3 py-1.5 text-xs font-medium text-emerald-950 hover:bg-emerald-400 disabled:cursor-not-allowed disabled:opacity-60"
        >
          {loading ? 'Signing in…' : 'Sign in'}
        </button>
      </form>
    </div>
  )
}

