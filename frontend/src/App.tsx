import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'
import { AuthPage } from './features/auth/AuthPage'
import { useAuth } from './authContext'

function AppShell() {
  const { user } = useAuth()

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50">
      <header className="border-b border-slate-800 bg-slate-950/70 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
          <span className="text-lg font-semibold tracking-tight">
            MUT H.A.I.F
          </span>
          <nav className="flex gap-4 text-sm text-slate-300">
            {user ? (
              <span className="text-xs text-emerald-300">
                {user.first_name || user.username} · {user.role}
              </span>
            ) : (
              <Link to="/auth" className="hover:text-emerald-400">
                Sign in
              </Link>
            )}
          </nav>
        </div>
      </header>
      <main className="mx-auto max-w-6xl px-4 py-8">
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/auth" element={<AuthPage />} />
        </Routes>
      </main>
    </div>
  )
}

function LandingPage() {
  return (
    <div className="space-y-6">
      <div>
        <p className="text-sm font-medium text-emerald-400">
          Hostel Allocation & Finance
        </p>
        <h1 className="mt-1 text-3xl font-semibold tracking-tight text-slate-50">
          Welcome to MUT H.A.I.F portal
        </h1>
        <p className="mt-3 max-w-2xl text-sm text-slate-300">
          Unified access for students, hostel administrators, and finance staff
          to manage allocations, room capacity, billing, and payments in one
          place.
        </p>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        <SectionCard
          title="Students"
          description="View eligibility, request hostel spaces, track allocations, invoices, and payments."
        />
        <SectionCard
          title="Hostel Admin"
          description="Manage hostels, rooms, and allocation workflows with real-time occupancy insight."
        />
        <SectionCard
          title="Finance"
          description="Configure hostel fee structures, manage invoices, and reconcile student payments."
        />
      </div>
    </div>
  )
}

type SectionCardProps = {
  title: string
  description: string
}

function SectionCard({ title, description }: SectionCardProps) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-4 shadow-sm shadow-slate-950/40">
      <h2 className="text-sm font-semibold text-slate-50">{title}</h2>
      <p className="mt-2 text-xs text-slate-300">{description}</p>
    </div>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <AppShell />
    </BrowserRouter>
  )
}
