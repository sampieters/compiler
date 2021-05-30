.data
string1_1: .asciiz "Enter a number:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "fib("
string3_2: .asciiz ")\t= "
string3_3: .asciiz ";\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        sw      $4, 4($fp)
        # BEGIN IF CONDITION
        lw      $8, 4($fp)
        slti    $8, $8, 2
        sw      $8, 8($fp)
        lw      $8, 8($fp)
        beq     $8,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        # END IF BODY
        b       $L1
        nop     
$L0:    
        # BEGIN ELSE BODY
        lw      $8, 4($fp)
        subi    $8, $8, 1
        sw      $8, 12($fp)
        lw      $4, 12($fp)
        jal     f
        lw      $8, 4($fp)
        subi    $8, $8, 2
        sw      $8, 16($fp)
        lw      $4, 16($fp)
        jal     f
        add     $8, $11, $14
        # END ELSE BODY
$L1:    
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        jr      $ra
                
main:   
        addiu   $sp, $sp, -52
        sw      $fp, 48($sp)
        sw      $ra, 44($sp)
        sw      $4, 40($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 24($fp)
        li      $v0, 5
        syscall 
        sw      $v0, 24($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        li      $9, 1
        sw      $9, 28($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $9, 28($fp)
        lw      $10, 24($fp)
        sle     $9, $9, $10
        sw      $9, 32($fp)
        lw      $9, 32($fp)
        beq     $9, $0, $L3
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $9, 28($fp)
        addi    $9, $9, 1
        sw      $9, 36($fp)
        lw      $9, 36($fp)
        sw      $9, 28($fp)
        lw      $4, 28($fp)
        jal     f
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string3_3
        li      $v0, 4
        syscall 
        j       $L2
        # END WHILE BODY
                
$L3:    
        move    $sp, $fp
        lw      $4, 40($sp)
        lw      $ra, 44($sp)
        lw      $fp, 48($sp)
        addiu   $sp, $sp, 52
        li      $v0, 10
        syscall 