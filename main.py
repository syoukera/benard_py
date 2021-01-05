from benard import benard

def main():
    sim = benard()

    maxit = 100
    imon = 5
    jmon = 5
    sormax = 1.0e-3
    source = 1.0e10


    for niter in range(maxit):

        sim.update()

        resorm = sim.resorm/sim.flowin
        resoru = sim.resoru/sim.xmonin
        resorv = sim.resorv/sim.xmonin
        # ayashi
        resort = sim.resort/sim.xmonin
        
        print(f'{niter} {resoru:.2e} {resorv:.2e} {resorm:.2e} ', end='')
        print(f'{sim.U[imon, jmon]:.2e} {sim.V[imon, jmon]:.2e} ', end ='')
        print(f'{sim.P[imon, jmon]:.2e} {sim.T[imon, jmon]:.2e}', end='\n')
        
        source = max(resorm, resoru, resorv, resort)
        
        if source < sormax:
            print('Converged!')
            break
            
        if niter == maxit-1:
            print('Not converged...')

if __name__ == '__main__':
    main()