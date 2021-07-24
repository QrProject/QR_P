import Image from 'next/image';
import styles from '@/styles/Headers.module.scss';

export default function headers () {
  return (
    <header className="headers">
      <Image
        className={styles.headers__img}
        src="/title_logo.jpg"
        alt="Main Logo"
        sizes="responsive"
        height={50}
        width={300}
      />
    </header>
  )
}